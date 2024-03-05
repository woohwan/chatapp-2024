import { getTextClaude } from './claude.js'

import express from 'express'
import bodyParser from 'body-parser'
import cors from 'cors'

const app = express()
const port = 8000
app.use(bodyParser.json())
app.use(cors())

app.post("/", async (req, res) => {
  const { chats } = req.body
})


getTextClaude("Hi", 0)
  .then((resp) => {
    console.log(resp)
  })
