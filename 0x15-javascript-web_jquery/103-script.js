$(document).ready(function(){
  $("#btn_translate").click(getTranslation);
  $("#language_code").keypress(function(event){
    if (event.which == 13) {
      getTranslation();
    }
  });
});

function getTranslation() {
  var languageCode = $("#language_code").val();
  $.getJSON("https://www.fourtonfish.com/hellosalut/hello/" + languageCode, function(data){
    $("#hello").text(data.hello);
  });
}
