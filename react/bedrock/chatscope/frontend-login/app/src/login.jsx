import React, { useState} from "react";
import { useNavigate } from "react-router-dom";


const Login = (props) => {
    const [ userId, setUserId ] = useState('')
    const [ userIdError, setUserIdError] = useState("")
    const [ password, setPassword ] = useState('')
    const [ passwordError, setPasswordError ] = useState('')
    const [ mfacode, setMfacode ] = useState("")
    const [ accountId, setAccountId ] = useState("")
    const [ token, setToken ] = useState("")

    const fitcloud_url = "https://aws-dev.fitcloud.co.kr"
    // const fitcloud_url = "http://fitcloud-dev-web-1949357121.ap-northeast-2.elb.amazonaws.com/"

    const navigate = useNavigate()

    const onButtonClick = () => {
        // You'll update this function later...
        // Set initial error values to empty
        setPasswordError("")

        // Check if the user ahs entered both field correctly
        if("" === userId) {
            setUserIdError("Please enter your userid")
            return
        }

        if ("" === password) {
            setPasswordError("Please enter a password")
            return
        }

        // Check if email has an account associated with it
        if (password.length < 7) {
            setPasswordError("The password must be 8 characters or longer")
            return
        }
        logIn()
    }

    // Log in a user using email and password
    // proxy test: 향후 fitcloud_url 넣을 것
    const logIn = async () => {
        const response = await fetch( fitcloud_url + "/login", {           
            method: "POST",
            credentials: "include",
            headers: {
                'Access-Control-Expose-Headers': '*',
                'Access-Control-Allow-Credentials': true,
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            body: JSON.stringify({"userId": userId, "password": password, "mfaCode": mfacode})
        })
        .then(r => r.json())
        .then(res => {
                console.log(res)
            }
        )
            // localStorage.setItem("userId", JSON.stringify({userId, accountId: accountId, token: s.sessionId}))
            
            // props.setLoggedIn(true)
            // props.setUserId(userId)
            // props.setAccountId("532805286864")   // 현재 API가 없어 고정 값으로
            // props.setToken(r.sessionId)
            // navigate("/")

        // }).catch (err => {
        //     console.log(err)
        // })
    }

    return (

        <div className={'mainContainer'}>
            <div className={'titleContainer'}>
                <div>Login</div>
            </div>
            <br />
            <div className={'inputContainer'}>
                <input
                    value={userId}
                    placeholder="Enter your userid here"
                    onChange={(ev)=>setUserId(ev.target.value)}
                    className={'inputBox'}
                />
                <label className="errorLabel">{userIdError}</label>
            </div>
            <br />
            <div className={'inputContainer'}>
                <input
                    value={password}
                    type="password"
                    placeholder="Enter your password here"
                    onChange={(ev)=>setPassword(ev.target.value)}
                    className={'inputBox'}
                />
                <label className="errorLabel">{passwordError}</label>
            </div>
            <br />
            <div className={'inputContainer'}>
                <input
                    value={mfacode}
                    placeholder="Enter your MFA Code here"
                    onChange={(ev)=>setMfacode(ev.target.value)}
                    className={'inputBox'}
                />
            </div>
            <br />
            <div className={'inputContainer'}>
                <input className={'inputButton'} type="button" onClick={onButtonClick} value={'Log in'} />
            </div>
        </div>

    )
}

export default Login