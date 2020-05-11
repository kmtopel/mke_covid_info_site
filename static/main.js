var submit_btn = document.getElementById('post-submit-btn');
var filter_btn = document.getElementById('filter-results');
var posts = document.getElementsByTagName('article');

function filter_results()
    {
    var choices = document.getElementById("post_type_filter");
    var selected_choice = choices.options[choices.selectedIndex].value;
    var display = document.getElementsByClassName(selected_choice);

    for (var i=0; i<display.length; i++)
        {
            display[i].style.display = 'inherit';
        }

    }