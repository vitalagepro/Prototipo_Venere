function showHideInput() {
    var select = document.getElementById("meseSelect");
    var calendarField = document.getElementById("calendarField");

    if (select.value === "3") { 
        calendarField.disabled = false; 
        calendarField.style.border = "1px solid #4CB9E7"; 
    } else {
        calendarField.disabled = true; 
        calendarField.style.border = "1px solid rgb(194, 227, 239)"; 
    }
}