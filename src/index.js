// console.log($, 1111111)

$("#button").click(function(){
  $.ajax({
    url:"http://127.0.0.1:6543/",
    success: function(result){
      const arr = JSON.parse(result)
      const imgArr = arr.map(v => $(`<img src=${v} alt=${v}/>`))
      $("#div1").html(imgArr);
    }
  });
});