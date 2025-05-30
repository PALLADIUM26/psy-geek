function func() {
    const ans=[];
    const res = [];

    for(let i=1; i<111; i++){
        ans.push(document.getElementById('q'+i).value);
    }
    for(let i=1; i<6; i++){
        res.push(document.getElementById('a'+i));
    }

    // const r1 = document.getElementById('a1');
    // const r2 = document.getElementById('a2');
    // const r3 = document.getElementById('a3');
    // const r4 = document.getElementById('a4');
    // const r5 = document.getElementById('a5');
    // console.log(ans)
    processFunc(ans, res);
    // const res = processFunc(ans);
    // console.log('lol')
    // console.log(res)
    
    // r1.textContent = `Anxiety: ${res[0]}`;
    // r2.textContent = `Independence: ${res[1]}`;
    // r3.textContent = `Extroversion: ${res[2]}`;
    // r4.textContent = `Tough Mindness: ${res[3]}`;
    // r5.textContent = `Self Control: ${res[4]}`;
}

function processFunc(ans, res) {
    const data = {
        answer: ans,
    };
    fetch('http://127.0.0.1:5000/predict', { // Replace '/submit' with your Python backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json()) // Assuming your Python backend returns JSON
    .then(responseData => {
        console.log('Success:', responseData);
        console.log(responseData.message1)
        console.log(responseData.message2)
        console.log(responseData.message3)
        console.log(responseData.message4)
        console.log(responseData.message5)

        // res.push(responseData.message1)
        // res.push(responseData.message2)
        // res.push(responseData.message3)
        // res.push(responseData.message4)
        // res.push(responseData.message5)
        // console.log(res)

        res[0].textContent = `Anxiety: ${responseData.message1}`;
        res[1].textContent = `Independence: ${responseData.message2}`;
        res[2].textContent = `Extroversion: ${responseData.message3}`;
        res[3].textContent = `Tough Mindness: ${responseData.message4}`;
        res[4].textContent = `Self Control: ${responseData.message5}`;

        // return res;
        // return responseData;
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("An error occurred. See console for details."); //Alert the user of an error.
    });
    
}