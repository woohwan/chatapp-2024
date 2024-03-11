import express from 'express'
import bodyParser from 'body-parser'
import cors from 'cors'
import { BedrockAgentRuntimeClient, InvokeAgentCommand } from '@aws-sdk/client-bedrock-agent-runtime'

// app setting
const app = express()
const port = 8000
app.use(bodyParser.json())
app.use(cors())

export const invokeBedrockAgent = async (prompt, accountId, token, sessionId) => {
  const client = new BedrockAgentRuntimeClient({ region: "us-east-1" })

  const agentId = "IUFLFZG1TW";
  const agentAliasId = "GDOGYNUEF9";

  const command = new InvokeAgentCommand({
    sessionState: {
      sessionAttributes: {
        "token": token,
        "accountId": accountId
      }
    },
    agentId,
    agentAliasId,
    sessionId,
    inputText: prompt
  })

  try {
    let completion = ""
    const response = await client.send(command)

    if (response.completion === undefined) {
      throw new Error("Completion is undefined")
    }

    for await (let chunkEvent of response.completion) {
      const chunk = chunkEvent.chunk
      const decodedResponse = new TextDecoder('utf-8').decode(chunk.bytes)
      completion += decodedResponse
    }

    return { "role": "assistant", "content": completion }
  } catch (err) {
    console.error(err)
  }
}

app.post("/", async (req, resp) => {
  console.log(req.body)
  const { prompt, accountId, token, sessionId } = req.body
  console.log("prompt: ", prompt)

  const result = await invokeBedrockAgent(prompt, accountId, token, sessionId)
  console.log(result)
  resp.json({
    output: result
  })
})

app.listen(port, () => {
  console.log(`Listening on port ${port}`)
})