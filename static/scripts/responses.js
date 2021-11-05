function getBotResponse(input) {
    // Simple responses
    if (input == "hello" || input == "Hello" || input == "hi" || input == "Hi" ) {
        return "Hello there!";
    } else if (input == "goodbye" || input == "Goodbye" || input == "bye" || input == "Bye") {
        return "Let us know if you need anything else!";
    } else if (input == "Hi, I have a question!") {
      return "What's the question? Maybe we can help!"
    } else {
        return "Try searching this question in the search bar to the left.";
    }
}
