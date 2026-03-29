import os
import uuid
import logging
from io import BytesIO

import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

from classify import classify

app = FastAPI()
logger = logging.getLogger(__name__)

@app.post("/classify/")
async def classify_logs(file: UploadFile, background_tasks: BackgroundTasks):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV.")

    output_file = f"resources/output_{uuid.uuid4().hex}.csv"

    try:
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))

        if "source" not in df.columns or "log_message" not in df.columns:
            raise HTTPException(
                status_code=400,
                detail="CSV must contain 'source' and 'log_message' columns."
            )

        df["target_label"] = classify(list(zip(df["source"], df["log_message"])))
        logger.info("Classification complete, saving to %s", output_file)

        df.to_csv(output_file, index=False)
        background_tasks.add_task(os.remove, output_file)
        return FileResponse(output_file, media_type='text/csv', filename="classified_output.csv")

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Unexpected error during classification")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await file.close()