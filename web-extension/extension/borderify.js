async function phishingDetect(URL) {
    try {
        console.log("Input URL is: " + URL);
        var website = {
            url: '',
            rate: ''
        };
        website.url = URL;
        const result = await content.fetch('https://cors-anywhere.herokuapp.com/http://phishingman.pythonanywhere.com/result/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(website),
        });
        const data = await result.json();
        return data;
    } catch(error) {
        alert(error);
    }
}

var currentURL = String(window.location.href).replace(/^(https?:\/\/)?(www\.)?/,'');
var lastChar = currentURL[currentURL.length -1];
if (lastChar == "/") {
    currentURL = currentURL.substring(0, currentURL.length - 1);
}
console.log("currentURL is: " + currentURL);

phishingDetect("http://" + currentURL).then(data => {
    console.log(data);
    if (data.rate == "1") {
        document.body.style.border = "40px solid red";
        alert("Warning! This is a potential phishing website.");
    } else {
        document.body.style.border = "40px solid green";
        alert("Good News! This is a legitimate website.");
    }
});





