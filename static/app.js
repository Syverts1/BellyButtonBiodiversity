

function init() {
    var dropdown = document.getElementById("selDataset");
    var namesURL = "../names";

    d3.json(namesURL, function(error,response){
        // Handle errors
        if (error) return console.log(error);
        
        console.log(response)
        
        // Loop through response
        for(var i = 0 ; i <response.length; i++){
        var dropDownOption = document.createElement("option");

        var item = response[i];
        
        dropDownOption.innerHTML = item;
        
        dropdown.append(dropDownOption);
        
    };
        //Create PIE chart with data from /samples/<sample> and /otu to display the top 10 samples.

        console.log(response[0]);
        var sampleURL = "../samples/" + response[0];
        
        d3.json(sampleURL, function(error,sampleResponse){
            // Handle errors
            if (error) return console.log(error);
            
            topOtu = [];
            topSamples = [];

            for(var i = 0; i < 10; i++){
                topOtu.push(sampleResponse[0].otu_ids[i]);
                topSamples.push(sampleResponse[0].sample_values[i]);
            };
            //1. Use the OTU Description as the hovertext for the chart*/

            pieData = [{
                labels: topOtu,
                values: topSamples,
                type: 'pie' }];
            var pieLoc = document.getElementById("pieChart");
            Plotly.plot(pieLoc, pieData);
            
            //create bubble chart
            bubbleData = [{
                x: sampleResponse[0].otu_ids,
                y: sampleResponse[0].sample_values,
                mode: 'markers',
                marker: {
                    color: sampleResponse[0].otu_ids,
                    size: sampleResponse[0].sample_values }}];
            bubbleLayout = {
                xaxis: {
                    title: "OTU ID"
                },
                yaxis: {
                    title: "Sample Values"
                }
            };
            var bubbleLoc = document.getElementById("bubbleChart");
            Plotly.plot(bubbleLoc, bubbleData, bubbleLayout);
        });
            /*Create a Bubble Chart that uses data from your routes /samples/<sample> 

           2. -Use the OTU Description Data for the text values
           3. -Use Plotly.restyle to update the chart whenever a new sample is selected*/
        
        
        var metadataURL = "../metadata/" + response[0];

        d3.json(metadataURL, function (error, metadataResponse){
            if (error) return console.log(error);

            var meta = document.getElementById("meta");
            
            for (const [key, value] of Object.entries(metadataResponse[0])) {
                var contents = document.createElement("p");
                
                contents.innerHTML = key + ": " + value;
                contents.id = key;
                meta.append(contents);
                
              };
            
        })

})
};

//Use Plotly.restyle to update the chart whenever a new sample is selected
function optionChanged(querySample) {
    var pieLoc = document.getElementById("pieChart");
    
    var sampleURL = "../samples/" + querySample;
    
    d3.json(sampleURL, function(error,sampleResponse){
        // Handle errors
        if (error) return console.log(error);
        
        topOtu = [];
        topSamples = [];

        for(var i = 0; i < 10; i++){
            topOtu.push(sampleResponse[0].otu_ids[i]);
            topSamples.push(sampleResponse[0].sample_values[i]);
        };
        Plotly.restyle(pieLoc, "labels", [topOtu]);
        Plotly.restyle(pieLoc, "values", [topSamples]);
    });
    var metadataURL = "../metadata/" + querySample;

    d3.json(metadataURL, function (error, metadataResponse){
        if (error) return console.log(error);

        var meta = document.getElementById("meta");
        
        for (const [key, value] of Object.entries(metadataResponse[0])) {
            
            var contents = document.getElementById(key);
            
            contents.innerHTML = key + ": " + value;
            
          };
        
    })
    

};
  

init();