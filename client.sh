#!/bin/bash

while read FILE
do
	NAME=$(basename $FILE)
	OUTPUT="/data/outputs/mit_$NAME"
	curl -X 'POST' \
		"http://$MIT_API:8000/annotation/find_text_vars?text=With%20the%20current%20implementation%2C%20we%20have%20the%20ability%20to%20distinguish%20between%20the%20effects%20of%20NPI%20within%20the%20categories%20mentioned%20above.%20For%20the%20case%20in%20which%20multiple%20NPI%20within%20category%20III%20are%20implemented%2C%20we%20have%20implemented%20a%20value-added%20approach%20to%20calculating%20their%20effectiveness%20in%20reducing%20the%20basic%20reproduction%20number.%20In%20this%20case%2C%20we%20calculate%20the%20reduction%20in%20%F0%9D%91%850%20based%20on%20the%20number%20of%20NPIs%20in%20place.%20If%20one%20NPI%20is%20in%20place%2C%20%F0%9D%91%850%20is%20reduced%20by%2040%25.%20If%20two%20NPI%20are%20in%20place%2C%20%F0%9D%91%850%20is%20reduced%20by%2060%25.%20If%20three%20or%20more%20NPI%20are%20in%20place%2C%20then%20%F0%9D%91%850%20is%20reduced%20by%2070%25.&gpt_key=$OPENAI_KEY" \
		-H 'accept: application/json' \
		-d '' > $OUTPUT
done < <(find /data/inputs -type f)
