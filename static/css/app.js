const openNav = () => {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

const closeNav = () => {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}
function open_photo(photo) {
    document.getElementById("big-photo").innerHTML =
      ("<img onclick='close_photo()' style='position: absolute;' src='" + photo + "'>")
  }
  
function close_photo() {
    document.getElementById("big-photo").innerHTML = ""
  }