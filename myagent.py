import json
import logging
import boto3
from bedrock_agentcore import BedrockAgentCoreApp

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = BedrockAgentCoreApp()

bedrock = boto3.client("bedrock-runtime", region_name="ap-south-1")
MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"


@app.entrypoint
def invoke(payload):
    if isinstance(payload, (bytes, str)):
        try:
            payload = json.loads(payload)
        except Exception:
            payload = {}

    prompt = payload.get("prompt") or payload.get("input") or ""
    if not prompt:
        return {"message": "No prompt provided."}

    # Build messages list with only the current prompt (no history)
    messages = [
        {"role": "user", "content": [{"type": "text", "text": prompt}]}
    ]

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.7,
        "messages": messages,
    }

    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body),
        )
        reply = json.loads(response["body"].read())["content"][0]["text"]
    except Exception as e:
        logger.exception("Bedrock call failed")
        return {"message": f"Error: {e}"}

    return {"message": reply}


if __name__ == "__main__":
    app.run()