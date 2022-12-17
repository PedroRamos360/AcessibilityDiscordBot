import discord
import speech_recognition as sr

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!transcribe'):
        # Get the voice channel the user is in
        try:
            voice_channel = message.author.voice.channel
        except AttributeError:
            voice_channel = None
        if voice_channel is None:
            await message.channel.send('You are not in a voice channel!')
            return

        # Join the voice channel
        voice_client = await voice_channel.connect()

        # Start transcribing the audio
        while True:
            try:
                voice_channel = message.author.voice.channel
            except AttributeError:
                voice_channel = None
            if voice_channel is None:
                await voice_client.disconnect()
                return
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)

            # Transcribe the audio
            try:
                text = r.recognize_google(audio)
            except sr.UnknownValueError:
                await message.channel.send('Sorry, I couldn\'t understand what was said.')
                continue
            except sr.RequestError as e:
                await message.channel.send('Error: {0}'.format(e))

            # Disconnect from the voice channel and send the transcribed text
            await message.channel.send('Transcribed text: ' + text)

<<<<<<< HEAD
client.run('BOT TOKEN')
=======
client.run('meu token')
>>>>>>> refs/remotes/origin/main
