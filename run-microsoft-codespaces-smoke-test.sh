curl -sS -X POST "$AZURE_OPENAI_ENDPOINT/openai/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "'"$AZURE_OPENAI_DEPLOYMENT"'",
    "messages": [{"role":"user","content":"Ping Azure OpenAI"}]
  }'