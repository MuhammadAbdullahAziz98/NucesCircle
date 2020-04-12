var postCounter = 1;
currentColor1 = "#000000"
currentColor2 = "#000000"
currentColor3 = "#000000"
pageNo=2;
$(window).scroll(function() {   
    if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
            pageNo = pageNo + 1;   
            var link = $(this);
            var page = pageNo;
            $.ajax({
              type: 'post',
              url: '/lazy_load_posts/',
              data: {
                'page': page,
                'csrfmiddlewaretoken': window.CSRF_TOKEN // from index.html
              },
              success: function(data) {
                // if there are still more pages to load,
                // add 1 to the "Load More Posts" link's page data attribute
                // else hide the link
                if (data.has_next) {
                    link.data('page', page+1);
                } else {
                  link.hide();
                }
                // append html to the posts div
                $('#posts-section').append(data.posts_html);
              },
              error: function(xhr, status, error) {
                // error
              }
            });
        
    }
});
function changeColor(event) {
    var btn = document.getElementById(event);
    style = window.getComputedStyle(btn);
    currentColor = style.getPropertyValue('color'); 
    var val = currentColor.localeCompare("rgb(33, 37, 41)");
    //alert(val);
    if(val==0){
        btn.style.color = "rgb(0,123,255)";
    }
    else{
        btn.style.color = "rgb(33, 37, 41)";
    }
}
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});
function create_post() {
    console.log("create post is working!") // sanity check
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    
    $.ajax({
        url : "/post", // the endpoint
        type : "POST", // http method
        data : { text : $('#post-text').val()}, // data sent with the post request
        // handle a successful response
        success : function(json) {
            //alert(user.id)
            text = document.getElementById("post-text").value;
            fn = $('#firstN').text();
            ln = $('#lastN').text();
            name = fn+" "+ln;
//            alert(name);
            $('#post-text').val(''); // remove the value from the input
            prepPost(name,text);
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}
function prepPost(name,text){
    console.log("inpre");
    btnGroup = 
    "<div class=\"btn-group \" style=\"width: 100%;\"><button class=\" btn btn-custom-white border-black-button btn-sm\""+" type=\"button\" id=\"div1button1\" onclick=\"changeColor(this.id)\">"+"<i class=\"fas fa-thumbs-up\"></i> Like</button><button class=\"btn border-black-button "+"\"btn-custom-white btn-sm\" type=\"button\" id=\"div1button2\" onclick=\"changeColor(this.id)\"><i"+" class=\"fas fa-comment\"></i> Comment</button><button class=\"btn border-black-button btn-custom-white btn-sm\""+" type=\"button\" id=\"div1button3\" onclick=\"changeColor(this.id)\"><i"+"class=\"fa fa-share\"></i> Share</button></div>";
    
    $('#posts-top').prepend(' <div class="offset-1 col-10 post-card mb-2 ">   '+ 
    '<div class="post-background">'+
        '<div class="card-body pb-1 border-for-post">'+
            '<span>'+
            '<span class="h6 pt-4 pl-2 card-title">'+ name +'</span>'+
            '</span>'+
            '<p class="pt-3 card-text">'+text +'</p>'+btnGroup+'</div></div></div></div>');
}
