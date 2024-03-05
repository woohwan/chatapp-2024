import { BedrockRuntime } from "@aws-sdk/client-bedrock-runtime";

const textDecoder = new TextDecoder("utf-8");
export const getTextClaude = async (prompt, temperature) => {
  const bedrock = new BedrockRuntime({
    region: "us-east-1",
  });

  const params = {
    modelId: "anthropic.claude-v2:1",
    contentType: "application/json",
    accept: "application/json",
    body: JSON.stringify({
      prompt: `\n\nHuman:\n  ${prompt}\n\nAssistant:\n`,
      max_tokens_to_sample: 2048,
      temperature: temperature || 0.5,
      top_k: 250,
      top_p: 1,
      stop_sequences: ["\\n\\nHuman:"],
    }),
  };

  const data = await bedrock.invokeModel(params);

  if (!data) {
    throw new Error("AWS Bedrock Claude Error");
  } else {
    const response_body = JSON.parse(textDecoder.decode(data.body));
    return response_body.completion;
  }
};