function f(){
    var image =  document.getElementById("image")
    var width = document.getElementById('width').value;
    var height = document.getElementById('height').value;
    if (document.getElementById("widthCheckBox").checked)
        image.width = width
    if (document.getElementById("heightCheckBox").checked)
        image.width = height
    var selectVoiture = document.getElementById('selectVoiture').value;
    image.src = selectVoiture ;
}
