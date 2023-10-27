<script setup>
console.log("About page has been loaded!");
import Sidebar from '../components/Sidebar.vue';  
</script>


<template>
  <Sidebar></Sidebar>
  <div class="md:pl-[260px]">
    <h1 class=" title-container
                text-4xl
                font-semibold
                text-center
              
                sm:pt-[20vh]
                ml-auto
                mr-auto
               
               
                flex
                gap-2
                items-center
                justify-center
              ">
      WebGPT
    </h1>
    <div class="content-container2">
      <div class="box ">
        <p class="box-text ">
          While <b>ChatGPT</b> stands as one of the most advanced chatbots, it operates without a direct link to internet.
          Recognizing this gap, GPT WEB was conceived. <br />Welcome to <b>WebGPT</b>, where the limitations of static knowledge
          meet the boundlessness of the internet.
          <br /> <br /><p class="bold underline">How It Works:</p>
        </p>
        <ol class="box-text">
          <li>1) User Interaction: Users initiate a conversation or ask a question through our intuitive interface.</li>
          <li>2) Initial Assessment: The system evaluates the query to determine if it requires real-time data from the
            BING Search API.</li>
          <li>3) Search Integration: Should the system identify the need, a web search is triggered to fetch the latest
            information related to the user's query.</li>
          <li>4) Informed Response Generation: Results from the search are melded with the initial question, allowing for
            a more informed response to be crafted.</li>
          <li>5) User Feedback: A comprehensive and current answer is presented to the user. With GPT WEB, we've created a
            bridge between vast static knowledge and dynamic real-time updates, ensuring users always receive the most
            pertinent information.</li>
        </ol>
        <br />
        <ul class="box-text"><p class="bold underline">Tech Stack:</p>
          <li>- Frontend: Vue.js</li>
          <li>- Backend: Flask.py</li>
          <li>- Front-Back connection : Axios</li>
          <li>- APIs: OpenAI's ChatGPT and BING Search API</li>
          <li>- Cloud hosting: Microsoft Azure Cloud</li>
        </ul>
        <br />
        
        <p class="box-text">
        
          <p class="bold underline">WebGPT Team:</p>
          <p class="authors">
            &nbsp;&nbsp;&nbsp;PONDEVIE Sam<br>
            &nbsp;&nbsp;&nbsp;TAVANI Lucas<br>
            &nbsp;&nbsp;&nbsp;PRADIE Corentin<br>
        </p>
        </p>
      </div>
    </div>
  </div>
</template>

<style>
.title-container {
  text-align: center;
  background-color: #1f2937;
  color: white;
}

.content-container1 {
  text-align: center;
  justify-content: center;
  background-color: #1f2937;
}

.content-container2 {
  text-align: center;
  flex-direction: column;
  height: 80vh;
  display: flex;
  justify-content: center;
  background-color: #1f2937;
}

.box {
  background-color: #2e3845;
  padding: 20px;
  border-radius: 10px;
  max-width: 80%;
  text-align: justify;
  margin: 0 auto;

}


.box-text {
  color: #fff;
  font-size: 15px
}

.title {
  font-size: 40px;
  color: #fff;
}

.authors {
  color: white;
  /* font-weight: 600; */
  font-size: 18px;
}
.bold {
  font-weight: 600;
 
  color: white;
}

.underlined {
  text-decoration: underline;
}
</style>