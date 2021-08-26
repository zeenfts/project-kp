var today = new Date();
var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate() + " " + today.getHours() + ":" + today.getMinutes();
document.getElementById("currentDate").value = date;

document.getElementById("txtSntmt1").defaultValue = "Menurut saya magang di STARSHARE sudah sangat baik terutama bagi yang secara remote";