var input = document.getElementsByTagName("div")
for (i = 0; i < input.length; i++) {
    try {
        if (input[i].getAttribute("data-testid") == "new-post-button") {
            input[i].click();
            break;
        }
    } catch {
        var a = 58;
    }
}

