import { useState, useEffect }  from 'react'
import './App.css'
import '@chatscope/chat-ui-kit-styles/dist/default/styles.css';
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator
} from '@chatscope/chat-ui-kit-react'

const App = () => {
  let now = new Date()
  
  const [messages, setMessages ] = useState([
      {
        message: "안녕하세요? FitCloud 도우미입니다. 고객님의 문의에 최선을 다하겠습니다.",  
        sentTime: now.toLocaleDateString(),
        sender: "FitCloud",
        direction: "incoming",   // from AI
        position: "first",
      }
    ])
   
    const accountId = "532805286864"
    const token = "CC45380CB7656AF3880CF350183E96B7"


  // Backend URL: Lambda or API gateway URL
  const Backend_Url = 'http://localhost:8000/'

  const [isTyping, setIsTyping ] = useState(false)

  // user send message to ai. 
  const handleSendRequest = async (message) => {
    const newMessage = {
      message,
      direction: 'outgoing',
      sender: 'user'
    }

    setMessages((prevMessage) => [...prevMessage, newMessage])  // Chat history
    setIsTyping(true)     // AI typing으로 전환

    try {
      let response = await processMessageToBackend(message)
      // backend send: { output: { "role": "assistant", "content": completion } }
      const content = response.output.content
      console.log("content: ", content)
      if (content) {
        const chatResponse = {
          message: content,
          direction: 'incoming',
          sender: 'FitCloud',
          position: 'first'
        }
        setMessages((prevMessage) => [...prevMessage, chatResponse]) // Chat UI에 Display
      }
    } catch(err) {
      console.log("Error processing message: ", err)
    } finally {
      setIsTyping(false)
    }
  }

  const processMessageToBackend = async (user_message) => {
    
    const prompt = user_message
    const body = {
      "prompt": prompt,
      "accountId": accountId,
      "token": token,
      "sessionId": "s-01"
    }

    const response = await fetch(Backend_Url, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body)
    })

    return response.json()
  }

  return (
    <div className='App'>
      <div style={{ position: "relative", height: "600px", width: "500px"}}>
        <div>
          <h3>FitCloud Chatbot 도우미</h3>
        </div>
        <MainContainer>
          <ChatContainer>
            <MessageList
              scrollBehavior='smooth'
              typingIndicator={ isTyping ? <TypingIndicator content="FitCloud is typing" /> : null }
              >
                {messages.map( (message, i) => {
                  // role에 따라 text alignment 조정
                  if (message.sender == 'FitCloud') {
                    return <Message key={i} model={message} className='ai-message' />
                  } else {
                    return <Message key={i} model={message} className='user-message' />
                  }
                  
                })}
            </MessageList>
            <MessageInput  attachButton={false} placeholder='Send a Message' className='message_input' onSend={handleSendRequest} />
          </ChatContainer>
        </MainContainer>
      </div>
    </div>
  )
}

export default App