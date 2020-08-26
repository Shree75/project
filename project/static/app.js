$(function () {
  $.ajax({
    url: "patients.json",
    dataType: "json",
    type: "get",
    cache: false,
    success: function (data) {
      $(data.patients).each(function (index, value) {
        setInterval(1000);
        console.log("hi");
        alert(value.patients);
        setInterval(350);
        alert(value.death);
      });
    },
  });
});
