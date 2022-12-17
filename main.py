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
        while voice_client.is_connected():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)

            # Transcribe the audio
            try:
                text = r.recognize_google(audio)
            except sr.UnknownValueError:
                text = "Sorry, I couldn't understand"
                await message.channel.send('Sorry, I couldn\'t understand what was said.')
            except sr.RequestError as e:
                await message.channel.send('Error: {0}'.format(e))

            # Disconnect from the voice channel and send the transcribed text
            await message.channel.send('Transcribed text: ' + text)

client.run('MTA1MjI2NDg5ODA1MjIzNTI5NQ.GYCko9.Cu2O7EmQDM7pYMayh6SEHoldRPItd413isQFu4')