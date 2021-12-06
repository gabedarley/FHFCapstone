async function getBotResponse(input) {
  // Simple responses
  if (input == "hello" || input == "Hello" || input == "hi" || input == "Hi") {
    return "Hello there!";
  } else if (input == "goodbye" || input == "Goodbye" || input == "bye" || input == "Bye") {
    return "Let us know if you need anything else!";
  } else if (input == "Hi, I have a question!") {
    return "What's the question? Maybe we can help!"
  } else {
    let url = 'http://127.0.0.1:5000/answer';
    let data = { "message": input };
    // let request = new XMLHttpRequest();
    // request.open('POST', url);
    // request.setRequestHeader("Accept", "application/json");
    // request.setRequestHeader("Content-Type", "application/json");
    // let answer = null;
    // request.onload = function () {
    //   if (request.readyState === 4) {
    //     console.log(request)
    //     answer = request.response;
    //   }
    // };
    // request.send(JSON.stringify(data));
    try {
      const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      if (response.status === 200) {
        const responseBot = await response.text()
        return responseBot;
      }
    } catch (error) {
      console.log(e)
    }
    return null;
  }
}
