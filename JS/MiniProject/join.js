const form = document.getElementById("form")

form.addEventListener("submit", function(event){
    event.preventDefault()

    let userID = event.target.id.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userEmail = event.target.email.value

    const idRegex = /^[a-zA-Z0-9]{6,12}$/;
    const pwRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    if (!idRegex.test(userID)) {
        alert("아이디는 6~12자의 영문자와 숫자로만 입력해주세요.");
        return;
    }

    if (!pwRegex.test(userPw1)) {
        alert("비밀번호는 8자 이상이며, 대문자, 소문자, 숫자, 특수문자를 모두 포함해야 합니다.");
        return;
    }
    
    if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다.")
        return
    }

    let userInfo = `
        아이디: ${userID}
        이름: ${userName}
        이메일: ${userEmail}
    `;

    alert("회원가입이 완료되었습니다!\n\n" + userInfo);

    // Optional: Redirect to another page after successful registration
    window.location.href = "1.html";
})