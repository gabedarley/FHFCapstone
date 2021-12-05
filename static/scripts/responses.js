function getBotResponse(input) {
    // Simple responses
    if (input == "hello" || input == "Hello" || input == "hi" || input == "Hi" ) {
        return "Hello there!";
    } else if (input == "goodbye" || input == "Goodbye" || input == "bye" || input == "Bye") {
        return "Let us know if you need anything else!";
    } else if (input == "Hi, I have a question!") {
      return "What's the question? Maybe we can help!"
    } else {
      let url = 'https://127.0.0.1:5000/answer';
      let request = new XMLHttpRequest();
      request.open('POST', url);
      request.setRequestHeader("Accept", "application/json");
      request.setRequestHeader("Content-Type", "application/json");
      let answer = null;
      request.onload = function() {
        answer = request.response;
      };

      let data = "{'message': 'What is IEP?'}";

      request.send(data);
      console.log(answer);
      return answer;
      //return "Try searching this question in the search bar to the left.";
    }
}
