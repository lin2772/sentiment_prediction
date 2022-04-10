// Initialize butotn with users's prefered color
let button = document.getElementById("predict").addEventListener('click',function(){
  var input = document.getElementById("input");
  console.log(input.value);
  processMessage(input.value) ;
  

});

function processMessage(message) {     
  const Http = new XMLHttpRequest();     
  message = "[\'"+message+"\']"
  console.log(message);
  var link = 'https://wm22vwpv8f.us-east-1.awsapprunner.com/columns/tweet/data/' + encodeURIComponent(message);
  console.log(link);
  Http.open("GET", link);
  Http.send();

  Http.onreadystatechange = function(){
    if(this.readyState==4 && this.status==200){
      var resultStr = JSON.stringify(Http.responseText);
      
      var data = JSON.parse(Http.responseText);
      console.log(data["results"]);
      var result = "No result";
      if(resultStr.includes("[0]")){
        result =  "No hate speech detected";
      }else if(resultStr.includes("[1]")){
        result =  "Possible hate speech";
      }
      var output = document.getElementById("output");
      output.value = result;
    }
  }
}
