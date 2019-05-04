// console.log($, 1111111)

$("#button").click(function(){
  $.ajax({
    url:"http://0.0.0.0:6543/",
    success: function(result){
      $("#div1").html(result);
    }
  });
});