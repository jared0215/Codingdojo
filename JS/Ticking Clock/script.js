function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() + 
        new Date().getMinutes() * 60 + 
        new Date().getHours() * 3600;
    }

    setInterval( function() {
    var time = getSecondsSinceStartOfDay();
    console.log(time);
    var rotateSeconds = document.getElementById("seconds");
    
}, 1000);