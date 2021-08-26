var today = new Date();
var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate() + " " + today.getHours() + ":" + today.getMinutes();
document.getElementById("currentDate1").value = date;
var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate() + " " + today.getHours() + ":" + (today.getMinutes()-7);
document.getElementById("currentDate2").value = date;

document.getElementById("txtCmpr1").defaultValue = "Mohon maaf sepertinya sedang ada maintenance ya?";
document.getElementById("txtCmpr2").defaultValue = "apakah website ada maintenance? karena error not found daritadi";