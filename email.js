//list of invalid domains
let invalidDomains = [
  "yahoo.com",
  "gmail.com",
  "outlook.com",
  "google.com",
  "hotmail.com",
  "me.com",
  "icloud.com",
  "aol.com",
  "gmx.com",
  "mac.com",
  "live.com",
  "comcast.com",
  "googlemail.com",
  "msn.com",
  "hotmail.co.uk",
  "yahoo.co.uk",
  "facebook.com",
  "verizon.net",
  "att.net",
  "gmz.com",
  "mail.com",
  "protonmail.com",
];

function emailCheck(event) {
  //Collecting user input and turning it to lower case
  var email = document.getElementById("email").value;
  let input = email.toLowerCase();
  // stop refresh on button press
  event.preventDefault();
  //email formatting
  const validRegex =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  //Splitting the email into two parts
  let splitter = input.split("@");
  //getting the part of the email that has domain name
  let domain = splitter[1];

  //Checking not an undefined value
  if (typeof input !== undefined) {
    //if input null - error
    if (input === null) {
      console.error("Please enter your email");
      return;
    }
    //if no input - error
    if (input == "") {
      console.error("Please enter your email");
      return;
    }
    //if text doesn't match regex, go through error
    if (!input.match(validRegex)) {
      console.error("Please enter a valid email");
      return;
    }
    //if text does match regex, go through this if statement
    if (input.match(validRegex)) {
      //loops through the lists of domains and compares the one entered
      for (let i = 0; i < invalidDomains.length; i++) {
        //if there is a match return error
        if (domain == invalidDomains[i]) {
          console.error("Please enter a corporate email");
        }
      }
      return;
    }
    //if input doesn't satisfy any of the if statements, return nothing - successful
    else {
      return;
    }
  }
  console.error("Sorry, something went wrong");
  return;
}
