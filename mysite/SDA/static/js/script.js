let audioButton = document.querySelector('.audio-button');   // <-- Change CSS Class Here
       audioButton.addEventListener('click', function(){
        var audio = document.getElementById("audio");

         if (audio.paused) {
            audio.play();
        }else{
            audio.pause();
            // audio.currentTime = 0
        }
      });