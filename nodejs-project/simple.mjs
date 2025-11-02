// simple.mjs - calls openai to write a story
// remember to set your OPENAI_API_KEY as an environment variable

import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-5",
    input: "Write a one-sentence bedtime story about a unicorn."
});

console.log(response.output_text);
