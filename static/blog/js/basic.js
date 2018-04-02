/*!
 * basic JavaScript/JQuery functions for results application
 */


// Toggle <div> based on div_id:
// Hidden div is defined in html with <a class="DivToggler" and id="div_id"> </a>
// Inside the <a></a> tags, an image (open/closed.gif) is defined.
// When this image is clicked, the div toggles on or off.
var divs = [];
$(document).ready(function() {

    $(".DivToggler").click(function(e) {
      e.preventDefault();

      var div_id = '.'+$(this).attr('id');


      if ($.inArray(div_id, divs) > -1 ) {
        divs.splice(div_id, 1);


      } else {
        divs.push(div_id);

      }

      $(div_id).toggle();

    });

});



// Toggle the image:
// Takes img.src which is src='{% static "results/images/closed.gif" %}'
// and parses the file name out of this path. If it is open.gif, then
// it toggles to closed.gif (using the path argument passed from onclick in html)
function ToggleImage(img) {

  var image = img.src;

  var img_path = image.split('/')
  var path = img_path.slice(3, -1).join('/')


  if (image.indexOf("closed") >=0) {
    img.src = "/" + path + "/open.gif";

  }

  else if (image.indexOf("open") >=0)

  {
    img.src = "/" + path + "/closed.gif";

  }

}


// Toggle the image:
// Takes img.src which is src='{% static "results/images/closed.gif" %}'
// and parses the file name out of this path. If it is open.gif, then
// it toggles to closed.gif (using the path argument passed from onclick in html)
function ToggleValue(val) {

  var value = val.value;

  if (value == '>') {
    val.value = "v";

  }
  else if (value == 'v')

  {
    val.value = ">";

  }

}



function CheckRadio(){

  var e=document.getElementById("machine-btn").checked;
      //alert(e);
      if(!e){
      alert("Machine radio button NOT selected");
          return false;
      }

}








''
