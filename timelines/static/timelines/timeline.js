function startCountDown(id, startDate, endDate) {
    updateCountDown(id, startDate, endDate);
    var x = setInterval(function() {
        updateCountDown(id, startDate, endDate);
    }, 1000);
}

function updateCountDown(id, startDate, endDate) {
    var badge = document.getElementById("timeCounter" + id);
    var card = document.getElementById("card" + id);
    if (badge == null || card == null) {
        return;
    }
    var now = new Date().getTime();
    if (now < startDate) {
        badge.innerHTML = "Starts in " + dateDifferenceAsString(startDate - now);
        badge.classList.add("text-dark");
        card.classList.add("bg-warning");
        card.classList.add("text-dark");
    } else if (now < endDate) {
        badge.innerHTML = "Ends in " + dateDifferenceAsString(endDate - now);
        badge.classList.add("text-white");
        card.classList.add("bg-success");
        card.classList.add("text-white");
    } else {
        badge.innerHTML = "Ended " + dateDifferenceAsString(now - endDate) + " ago";
        badge.classList.add("text-white");
        card.classList.add("bg-dark");
        card.classList.add("text-white");
    }
}


function dateDifferenceAsString(distance) {
    var distanceDate = new Date(distance);
    var years = distanceDate.getFullYear() - 1970;
    var months = distanceDate.getMonth();
    var days = distanceDate.getDate() - 1;
    var hours = distanceDate.getHours();
    var minutes = distanceDate.getMinutes();
    var seconds = distanceDate.getSeconds();
    var stringParts = [];
    if (years > 0) {
        stringParts.push(years + " years");
    }
    if (months > 0) {
        stringParts.push(months + " months");
    }
    if (days > 0) {
        stringParts.push(days + " days");
    }
    if (hours > 0) {
        stringParts.push(hours + " hours");
    }
    if (minutes > 0) {
        stringParts.push(minutes + " minutes");
    }
    if (seconds > 0) {
        stringParts.push(seconds + " seconds");
    }
    return stringParts.join(", ");
}