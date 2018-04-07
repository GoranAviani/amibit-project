var screen_width = window.innerWidth;
var screen_height = window.innerHeight;

// dashboard- on open focus to search field. by id
window.onload = function() {
document.getElementById("personal_assistant_search").focus();
  if(screen_width <= 768) {
    document.getElementById("ListofNotes").style.display = "none";
    document.getElementById("ListofLinks").style.display = "none";
  }
};

// for html : <button onclick="myFunction()">Try it</button>

function toggle_notes() {
    var x = document.getElementById("ListofNotes");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function toggle_links() {
    var x = document.getElementById("ListofLinks");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
