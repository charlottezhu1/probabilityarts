console.log("aaa");

// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }
// const csrftoken = getCookie("csrftoken");

// function generateGraph() {
//   var baseImage = document.getElementById("baseImage").value;
//   var distribution = document.getElementById("distribution").value;
//   var n = document.getElementById("n").value;

//   var data = {
//     baseImage: baseImage,
//     distribution: distribution,
//     n: n,
//   };

//   fetch("", {
//     method: "POST",
//     credentials: "same-origin",
//     headers: {
//       Accept: "application/json",
//       "X-Requested-With": "XMLHttpRequest", //Necessary to work with request.is_ajax()
//       "X-CSRFToken": csrftoken,
//     },
//     body: JSON.stringify(data),
//   })
//     .then((res) => res.json())
//     .then((data) => {
//       // console.log("Data sent to Django:", data);
//     });

//   // Use these variables to generate the graph or pass them to your backend for processing
//   console.log(data);
//   console.log("Base Image:", baseImage);
//   console.log("Distribution:", distribution);
//   console.log("Number of Samples:", n);
// }
