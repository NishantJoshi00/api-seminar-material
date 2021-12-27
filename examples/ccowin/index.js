let form = document.getElementById("the_form");

form.onsubmit = function(e) {
    e.preventDefault();
    ccowin();
};


function ccowin() {
    let form = document.getElementById("the_form");
    let pin = form.elements["pin"].value;
    // Get todays date, as string in %d-%m-%Y format
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth()+1;
    let yyyy = today.getFullYear();
    if( dd < 10 ) {
        dd = '0'+dd
    }
    if( mm < 10 ) {
        mm = '0'+ mm
    }
    today = dd + '-' + mm + '-' + yyyy; 

    let url = `https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=${pin}&date=${today}`
    console.log(url)

    // Let's make a API call to GET the data
    fetch(url, {method: 'GET'})
        .then(async function(response) {
            output = await response.json()
            for (center of output.centers) {
                for (session of center.sessions) {
                    if (session.date == today && session.vaccine == "COVISHIELD") {
                        document.getElementById("output").innerHTML = "AVAILABLE!";
                        document.getElementById("output").style.color = "green";
                        return;
                    }
                }
            }
            document.getElementById("output").innerHTML = "NOT AVAILABLE!";
            document.getElementById("output").style.color = "red";
        })
}