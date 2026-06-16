
import asyncio
import edge_tts
import os

# Voice Selection: Telugu Male
VOICE = "te-IN-MohanNeural"

# Scene Data with Acting Directions
scenes = [
    {
        "filename": "01_thirst_relief.mp3",
        "text": "అబ్బా! ఈ నీళ్లు చూస్తుంటే ప్రాణం లేచి వస్తుంది! చిన్న చీమ... కానీ దాహం పెద్ద!",
        "rate": "-10%",  # Slower (Relief)
        "pitch": "-2Hz"  # Slightly deeper
    },
    {
        "filename": "02_drowning_panic.mp3",
        "text": "అయ్యో! జారి పడిపోయా... స్విమ్మింగ్ నేర్చుకోవాల్సింది! హెల్ప్! ఈ నీళ్లు చాలా స్ట్రాంగ్!",
        "rate": "+25%",  # Fast (Panic)
        "pitch": "+5Hz"  # High pitch (Fear)
    },
    {
        "filename": "03_rescue_happy.mp3",
        "text": "ఆకు? హమ్మయ్య! థాంక్స్ ఫ్రెండ్, నన్ను కాపాడావు! యిప్పీ! ఫ్రీ రైడ్!",
        "rate": "+10%",  # Slightly fast (Excitement)
        "pitch": "+2Hz"  # Happy lift
    },
    {
        "filename": "04_threat_angry.mp3",
        "text": "ఒరేయ్! నా ఫ్రెండ్ నే చంపాలనుకుంటున్నావా?",
        "rate": "-15%",  # Slow (Serious/Threatening)
        "pitch": "-5Hz"  # Deep (Heroic/Angry)
    },
    {
        "filename": "05_bite_action.mp3",
        "text": "నేనుండగా... టేక్ దిస్! అయ్యో... ఈ పైన నా కాలు!",
        "rate": "+30%",  # Very Fast (Action)
        "pitch": "+0Hz"  # Normal pitch
    },
    {
        "filename": "06_ending_sassy.mp3",
        "text": "హా! పారిపో! మేము ఫ్రెండ్స్ ఇక్కడ... జాగ్రత్త! మంచి చేస్తే... మంచే జరుగుతుంది!",
        "rate": "-5%",  # Relaxed (Confident)
        "pitch": "-2Hz"  # Warm tone
    }
]


async def generate_scene_audio():
    print(f"🎙️  Using Voice: {VOICE}\n")

    for scene in scenes:
        print(f"Generating {scene['filename']}...")

        # Construct SSML with Acting Directions
        ssml_text = (
            f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='te-IN'>"
            f"<voice name='{VOICE}'>"
            f"<prosody rate='{scene['rate']}' pitch='{scene['pitch']}'>"
            f"{scene['text']}"
            f"</prosody>"
            f"</voice>"
            f"</speak>"
        )

        try:
            communicate = edge_tts.Communicate(ssml_text, VOICE)
            await communicate.save(scene['filename'])
        except Exception as e:
            print(f"❌ Error generating {scene['filename']}: {e}")

    print("\n✅ All scenes generated successfully!")


if __name__ == "__main__":
    asyncio.run(generate_scene_audio())
