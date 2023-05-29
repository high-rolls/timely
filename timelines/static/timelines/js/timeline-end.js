var addEventButton = document.getElementById("addEventButton");
addEventButton.addEventListener("click", function() {
    var start_date = document.getElementById("start_date");
    var end_date = document.getElementById("end_date");
    var currentDate = new Date();
    var formattedStartDate = currentDate.toISOString().split("T")[0];
    // format the date is yyyy-mm-dd, with zero-padding
    start_date.value = formattedStartDate;
    // add 1 day to the current date
    currentDate.setDate(currentDate.getDate() + 1);
    var formattedEndDate = currentDate.toISOString().split("T")[0];
    end_date.value = formattedEndDate;
    console.log(formattedStartDate);
});

var start_date = document.getElementById("start_date");
start_date.addEventListener("input", function() {
    var end_date = document.getElementById("end_date");
    var date = new Date(start_date.value);
    date.setDate(date.getDate() + 1);
    var formattedEndDate = date.toISOString().split("T")[0];
    end_date.value = formattedEndDate;
});

var end_date = document.getElementById("end_date");
end_date.addEventListener("change", function() {
    var start_date = document.getElementById("start_date");
    var startDate = new Date(start_date.value);
    var endDate = new Date(end_date.value);
    if (endDate < startDate) {
        alert("End date must be after start date.");
        end_date.value = start_date.value;
    };
});