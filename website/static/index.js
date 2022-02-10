const book_button=document.getElementById("book").addEventListener("click",(e)=>{

    var movieid = e.target.value;
    send_data(movieid);
    window.location = "http://127.0.0.1:5000/book_now";
})

function send_data(movieid){

    var xml = new XMLHttpRequest();
    var url= 'http://127.0.0.1:5000/helper';
    xml.open("POST", url, true);
    xml.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xml.send(movieid);

}

