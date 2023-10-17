<script setup>
import { openai } from "./openai/index";
import Guides from "./components/Guides.vue";
import Chat from "./components/Chat.vue";
import Sidebar from "./components/Sidebar.vue";
import { ref, onMounted, watch } from "vue";
import InputBar from "./components/InputBar.vue"; // Import the new component
import axios from 'axios';



let query = ref([]);
let response = ref([]);
const question = ref("");
const wrapper = ref([]);
const loading = ref(false);
const saveQuestions = ref([]);
const isLight = ref(false);

const getAnswer = async (message) => {
  console.log("Received in App.vue:", message);
  try {
    loading.value = true;
    wrapper.value.push({
      isAi: false,
      value: message,  // Use the passed-in message instead of question.value
    });
    wrapper.value.push({
      isAi: true,
      value: "|",
    });

    // Call to Flask server to get the response
    // OPTION 1 : ECHO THE MESSAGE
    // const flaskResponse = await axios.post('http://localhost:5000/chatbot-ask', { message: message });

    // OPTION 2 : CONVERSATION
    const flaskResponse = await axios.post('http://localhost:5000/chatbot-ask', { messages: wrapper.value.slice(0,-1)});


    console.log("Response from Flask:", flaskResponse.data); // Console log the response from Flask
    
    // Check for the response from Flask
    if (flaskResponse.data && flaskResponse.data.response) {
      let data = flaskResponse.data.response;  // Getting the response from Flask

      wrapper.value.pop();
      wrapper.value.push({
        isAi: true,
        value: data.trim(),
      });
    } else {
      throw new Error("No response from Flask server");
    }

    // Print Wrapper
    console.log('wrapper :')
    wrapper.value.forEach(element => console.log(element));
    console.log('fin wrapper:')

    let newquestions = wrapper.value.filter((item) => {
      return !item.isAi;
    });
  
    localStorage.setItem("threads", JSON.stringify(newquestions));
    getQuestions();

  } catch (error) {
    console.error("Error occurred:", error); // Console log any errors
    response.value = error.message || error;
  } finally {
    loading.value = false;
    question.value = "";
  }
};



const getQuestions = () => {
  saveQuestions.value = JSON.parse(localStorage.getItem("threads"));
};
const clearStorage = () => {
  saveQuestions.value = "";
  wrapper.value = [];
};

onMounted(() => {
  getQuestions();
});
</script>

<template>
  <div class="overflow-hidden w-full h-full relative" :class="isLight ? 'light' : 'dark'">
    
    <div class="flex flex-1 flex-col md:pl-[260px] h-screen">
      <main class="relative h-full w-full transition-width flex flex-col overflow-hidden items-stretch flex-1">
        <div class="h-full" v-if="wrapper.length">
          <div class="h-full flex-1 overflow-hidden">
            <div class="h-full overflow-y-auto dark:bg-gray-800">
              <div>
                <div class="flex flex-col items-center text-sm dark:bg-gray-800">
                  <div v-for="(chat, i) in wrapper" :key="i"
                    class="w-full border-b border-black/10 dark:border-gray-900/50 text-gray-800 dark:text-gray-100 group bg-gray-50 dark:bg-[#444654]"
                    :class="{ ai: chat.isAi }">
                    <Chat :chat="chat" :key="i" class="w-full" />
                  </div>
                  <div class="w-full h-32 md:h-48 flex-shrink-0"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <Guides v-else />
        <InputBar @submit="getAnswer" />
      </main>
    </div>
    <Sidebar :questions="saveQuestions" @clear="clearStorage()" @light="isLight = $event" />
  </div>
</template>

<style scoped></style>
