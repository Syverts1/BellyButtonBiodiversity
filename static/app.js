

function init() {
    var dropdown = document.getElementById("selDataset");
    var namesURL = "../names";

    d3.json(namesURL, function(error,response){
        // Handle errors
        if (error) return console.log(error);
        
        //console.log(response)
        
        // Loop through response
        for(var i = 0 ; i <response.length; i++){
        var dropDownOption = document.createElement("option");

        var item = response[i];
        
        dropDownOption.innerHTML = item;
        
        dropdown.append(dropDownOption);   
        };
        //Create PIE chart with data from /samples/<sample> and /otu to display the top 10 samples.

        //console.log(response[0]);
        var sampleURL = "../samples/" + response[0];
        
        d3.json(sampleURL, function(error,sampleResponse){
            // Handle errors
            if (error) return console.log(error);
            
            var otuURL = "../otu";
            d3.json(otuURL, function(error,otuResponse){
                if (error) return console.log(error);
                
                
                topOtu = [];
                topSamples = [];
                otuDescr = [];

                for(var i = 0; i < 10; i++){
                    topOtu.push(sampleResponse[0].otu_ids[i]);
                    topSamples.push(sampleResponse[0].sample_values[i]);
                    otuDescr.push(otuResponse[sampleResponse[0].otu_ids[i]]);
                };
                //console.log(topOtu)
                //console.log(otuDescr)

                pieData = [{
                    labels: topOtu,
                    values: topSamples,
                    type: 'pie',
                    hovertext: otuDescr
                 }];
                var pieLoc = document.getElementById("pieChart");
                Plotly.plot(pieLoc, pieData);
                
                var otuDescAll = [];
                for(i=0;i<sampleResponse[0].otu_ids.length;i++){
                    otuDescAll.push(otuResponse[sampleResponse[0].otu_ids[i]])
                }
                //create bubble chart
                bubbleData = [{
                    x: sampleResponse[0].otu_ids,
                    y: sampleResponse[0].sample_values,
                    text: otuDescAll,
                    mode: 'markers',
                    marker: {
                        color: sampleResponse[0].otu_ids,
                        size: sampleResponse[0].sample_values }}];
                bubbleLayout = {
                    xaxis: {title: "OTU ID"},
                    yaxis: {title: "Sample Values"}
                };
                var bubbleLoc = document.getElementById("bubbleChart");
                Plotly.plot(bubbleLoc, bubbleData, bubbleLayout);
        })}); //sample AND description d3.json
            /*Create a Bubble Chart that uses data from your routes /samples/<sample> 


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
            
        });

}) //close paren for names d3.json
}; //close paren for init

//Use Plotly.restyle to update the chart whenever a new sample is selected
function optionChanged(querySample) {
    var pieLoc = document.getElementById("pieChart");
    
    var sampleURL = "../samples/" + querySample;
    
    d3.json(sampleURL, function(error,sampleResponse){
        // Handle errors
        if (error) return console.log(error);

        var otuURL = "../otu";
        d3.json(otuURL, function(error,otuResponse){
            if (error) return console.log(error);
        
            topOtu = [];
            topSamples = [];
            otuDescr = [];

            for(var i = 0; i < 10; i++){
                topOtu.push(sampleResponse[0].otu_ids[i]);
                topSamples.push(sampleResponse[0].sample_values[i]);
                otuDescr.push(otuResponse[sampleResponse[0].otu_ids[i]]);
            };
            Plotly.restyle(pieLoc, "labels", [topOtu]);
            Plotly.restyle(pieLoc, "values", [topSamples]);
            Plotly.restyle(pieLoc, "hovertext", [otuDescr]);
    
            //replot bubble chart
            var otuDescAll = [];

            for(i=0;i<sampleResponse[0].otu_ids.length;i++){
                    otuDescAll.push(otuResponse[sampleResponse[0].otu_ids[i]])
                };

                //create bubble chart
                bubbleData = [{
                    x: sampleResponse[0].otu_ids,
                    y: sampleResponse[0].sample_values,
                    text: otuDescAll,
                    mode: 'markers',
                    marker: {
                        color: sampleResponse[0].otu_ids,
                        size: sampleResponse[0].sample_values }}];
                bubbleLayout = {
                    xaxis: {title: "OTU ID"},
                    yaxis: {title: "Sample Values"}
                };
                var bubbleLoc = document.getElementById("bubbleChart");
                Plotly.deleteTraces(bubbleLoc, 0);
                Plotly.plot(bubbleLoc, bubbleData, bubbleLayout);
        })});
   
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