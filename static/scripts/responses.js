function getBotResponse(input) {
    // Simple responses
    if (input == "hello" || input == "Hello" || input == "hi" || input == "Hi" ) {
        return "Hello there!";
    } else if (input == "goodbye" || input == "Goodbye" || input == "bye" || input == "Bye") {
        return "Let us know if you need anything else!";
    } else if (input == "Hi, I have a question!") {
      return "What's the question? Maybe we can help!"
    } else {
      let url = 'http://127.0.0.1:5000/answer?q=<user_question>';
      // let url = 'verse1.txt';
      let request = new XMLHttpRequest();
      request.open('GET', url);
      request.responseType = 'text';

      request.onload = function() {
        answer = request.response;
      };

      request.send();
      console.log(answer);
      return answer;
      //return "Try searching this question in the search bar to the left.";
    }
}
