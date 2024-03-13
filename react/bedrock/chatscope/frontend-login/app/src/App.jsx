import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Home from './home';
import Login from './login';
import Chat from './chat'
import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [loggedIn, setLoggedIn] = useState(false)
  const [userId, setUserId] = useState("")
  const [accountId, setAccountId] = useState("")
  const [token, setToken] = useState("")
  // const [password, setPassword] = useState("")
  // const [mfacode, setMfacode] = useState("")

  useEffect(() => {
    // Fetch the user email and token from local storage
    const user = JSON.parse(localStorage.getItem("userid"))

    // If the token/userid does not exist, mark the user as logged out
    if (!userId || !userId.token) {
      setLoggedIn(false)
      return
    }
  })
  

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home userId={userId} loggedIn={loggedIn} setLoggedIn={setLoggedIn}/>} />
          <Route path="/login" element={<Login setLoggedIn={setLoggedIn} setUserId={setUserId} />} />
          <Route path="/chat" element={<Chat userId={userId} loggedIn={loggedIn} setLoggedIn={setLoggedIn} accountId={accountId} token={token}/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;