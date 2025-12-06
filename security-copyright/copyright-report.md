# Section 1: Platform Analysis: YouTube’s Copyright System

YouTube has several tools that check uploads for copyrighted material. The main one is **Content ID**. When you upload a video, YouTube automatically scans the audio and video against files that labels and other rights holders have registered. If it finds a match, the owner of that material decides what happens next. They can block the video, run ads on it, or simply track how it performs.

YouTube also has a **Copyright Match Tool** that helps creators spot re-uploads of their own work. In addition, rights holders can send YouTube a manual takedown request through an online form. When a claim is made, YouTube tells the uploader and gives them a chance to dispute it. Most claims are handled automatically, but the final result depends on what the rights holder chooses. Some videos are blocked everywhere, while others are only restricted in certain countries.



# Section 2: Fair Use Experiments 

All screenshots are in the screenshots folder, and they are named with the experiment number followed by a short description. 

For this experiment, I chose blink-182's most popular song: I Miss You. I decided to use it's official video since songs are heavily coprighted. [Link To Song](https://www.youtube.com/watch?v=s1tAYmMjLdY&list=RDs1tAYmMjLdY&start_radio=1)

### 2.1: Experiment 1: Short Raw Clip (7 seconds)

**Description:**

I uploaded a 7-second unmodified clip from the Blink-182 “I Miss You” music video. This clip had no changes, commentary, or added text.

**Screenshots:**
`screenshots/exp1-checks.png`
`screenshots/exp1-upload.png`


**What happened:**
YouTube ran the automatic copyright check. The system reported “No issues found.” There were no Content ID claims, no blocks, and no monetization notices. The video was allowed with no restrictions.

**Timeline:**
Detection was immediate. The check completed in a few seconds.

**Outcome:**
Video allowed; No copyright claim; No monetization claim; No regional blocks; No actions required. 

---

### 2.2: Experiment 2: Longer Raw Clip (≈30 seconds)

**Description:**

I uploaded a longer section of the same music video, about 30 seconds. The clip was still unmodified.

**Screenshots:**
`screenshots/exp2-upload.png`
`screenshots/exp2-checks1.png`
`screenshots/exp2-checks2.png`

**What happened:**
YouTube’s Content ID system immediately detected copyrighted material. The rights holder allowed the video to remain on the platform, but a claim was placed on the content. This claim did not lead to a block or a strike.

**Timeline:**
Detection was instantaneous. YouTube flagged it during the upload checks.

**Outcome:**
Video allowed; Copyright-protected content found; Rights holder allows the content on YouTube; No visibility restrictions; Monetization status controlled by the rights holder; Options: “See details,” “Take action” (acknowledge, trim, or dispute)


---

### 2.3: Experiment 3: Clip with On-Screen Captions (Transformative Use)

**Description:**

I uploaded a short clip of the music video with added on-screen captions. This was meant to simulate commentary or analysis without narration.

**Screenshots:**
`screenshots/exp3-upload.png`
`screenshots/exp3-checks.png`

**What happened:**
YouTube completed the automatic check and reported no copyright issues. There were no claims. The added text may have reduced Content ID’s ability to match the clip, or the specific segment did not match the reference file in the database.

**Timeline:**
Immediate. Checks completed in a few seconds.

**Outcome:** Video allowed; No copyright claim; No visibility restrictions; No monetization or blocks; No actions required




---

# **Section 3: AI-Generated Content Investigation**

## **Experiment 1: Direct Reference Prompt**

**Prompt used:**
“Create an illustration of Pikachu wearing a scarf and walking in the snow.”

**What happened:**
This prompt failed every time. ChatGPT refused to generate the image and returned the message: **“This image generation request did not follow our content policy.”**
I tried multiple times, but the model rejected the request each time.

**Screenshot:**
N/A (It was totally blocked by ChatGPT.) 

**Platform response (YouTube):**
N/A (I could not generate the image at all). 

**Notes:**
This shows that the AI model itself blocks direct reproduction of copyrighted characters. The restriction happened before any platform enforcement. This is an interesting contrast with my fair use experiments, where YouTube scanned the uploads. Here, the AI tool enforced copyright protection at the generation stage.

---

## **Experiment 2: Style or Franchise Mimicry Prompt**

**Initial prompt:**
“In the style of Studio Ghibli, create a Christmas scene.”

**What happened:**
ChatGPT refused to generate this image as well, again due to policy restrictions. The message was the same as above.

**Revised approach:**
I switched to a different copyrighted reference. I asked for a Tetris-themed Christmas scene:
“Generate an illustration of Tetris, but with a Christmas effect.”

**Outcome:**
This prompt worked. ChatGPT generated a Christmas-themed Tetris illustration with falling blocks, snow, and holly decorations. The style suggested Tetris, but it did not copy an exact copyrighted design.

**Screenshot:**
`screenshots/AI-Tetris.png`

**Platform response (YouTube):**
For this part, I combined Experiment 2 and Experiment 3 in a short 10-second video and uploaded it to YouTube. It was simply a playback of the two images. YouTube did **not** flag it. There were no copyright claims, warnings, or visibility restrictions.

**Notes:**
This result shows that style-based or franchise-inspired prompts sometimes pass through the AI model, as long as the generated output does not reproduce a specific copyrighted asset. YouTube also did not detect any issue, even though Tetris is a well-known copyrighted property. I feel like it's because I did not include the Tetris logo. 

---

## **Experiment 3: Original Content Prompt (Control Group)**

**Prompt used:**
“Generate an abstract geometric landscape with bright colors and no recognizable characters.”

**Outcome:**
ChatGPT generated the image immediately. There were no warnings or refusals. The output is completely original and does not resemble any copyrighted character, artwork, or franchise.

**Screenshot:**
`screenshots/AI-Art.png`

**Platform response (YouTube):**
I uploaded the abstract image. YouTube did not flag it. There were no claims, warnings, or restrictions. (It was the same video as the Tetris one.) 

**Notes:**
This was the simplest upload of the three. Both the AI model and YouTube treated it the same as any regular image. 

---

## **Research Findings**

### **1. What ChatGPT’s Terms of Service Say About Copyright**

ChatGPT’s public guidelines explain that the model cannot create images of copyrighted characters or artwork unless the user has explicit permission. The tool is designed to avoid generating content that copies protected IP. It also avoids requests that try to mimic or recreate characters, scenes, logos, or visual assets from well-known franchises.
Instead, the model pushes users toward original creations or style-inspired content that does not replicate copyrighted material.

### **2. Who Owns the Copyright to AI-Generated Content?**

Based on current U.S. copyright law and OpenAI’s terms:

* **AI-generated content generally has no human author**, so it does not qualify for traditional copyright protection under U.S. law.
* OpenAI’s terms allow the user to *use* and *publish* the output, but that does not mean the user owns a copyright in the legal sense.
* Courts and the U.S. Copyright Office have consistently stated that works created by an AI system alone cannot receive copyright protection.
* If a user contributes meaningful creative input (for example, heavy editing), then parts of the work may qualify for copyright, but the AI-generated elements themselves do not.

So, the simplest explanation:
**I can use the images freely, but they are not copyrighted works owned by me or the AI company. They generally fall into a category with no copyright protection.**

### **3. YouTube’s Policy on AI-Generated Content**

YouTube does not treat AI-generated images differently from user-created images. As long as the upload does not contain copyrighted material that matches Content ID, the image is allowed.
There is no special tag, claim, or warning applied to AI content in this experiment. The platform only cares whether the uploaded video or image matches a copyrighted reference file in its system.

---






# **Section 4: Legal Analysis**

## **Fair Use Analysis Across Experiments**

### **Experiment 1: 7-Second Raw Clip**

**Purpose and character:**
The use was not transformative. It was a direct repost of a copyrighted music video. It had no commentary or new meaning. It was non-commercial, but this factor still weighs against fair use.

**Nature of the copyrighted work:**
The original work is creative and expressive. This factor weighs against fair use.

**Amount and substantiality:**
Only 7 seconds were used, which is a small portion, but even short clips can contain the “heart” of the work. This factor is neutral to slightly negative.

**Market effect:**
The clip is too short to replace the original song or video. It is unlikely to harm the market. This factor leans toward fair use.

**Overall:**
Under a strict legal analysis, this use probably would **not** qualify as fair use, because it is not transformative. YouTube’s system, however, did **not** detect the clip at all.

---

### **Experiment 2: 30-Second Raw Clip**

**Purpose and character:**
Again, the clip was unmodified and not transformative. This weighs strongly against fair use.

**Nature of the work:**
The source is a creative music video. This weighs against fair use.

**Amount and substantiality:**
Thirty seconds is a more substantial portion, especially for music. This factor weighs against fair use.

**Market effect:**
A 30-second continuous segment could substitute for part of the official video. This factor weighs against fair use.

**Overall:**
Legally, this clip is even less likely to qualify as fair use than the 7-second clip. YouTube’s system did detect copyrighted content here and applied a Content ID claim, although the rights holder chose to allow the video.

---

### **Experiment 3: Clip with Captions (Transformative Use Attempt)**

**Purpose and character:**
This clip included text overlays that provided commentary. Adding explanatory text changes the purpose from entertainment to analysis. This factor leans toward fair use.

**Nature of the work:**
The source remains creative, so this factor weighs slightly against fair use, but it does not override the transformation.

**Amount and substantiality:**
Only brief segments of the video were used, which supports fair use. The added text also breaks the continuous playback.

**Market effect:**
A commentary clip does not replace the original music video. It does not compete with the market for the song. This factor supports fair use.

**Overall:**
This is the strongest fair-use case of the three. However, YouTube’s system **did not detect** the copyrighted content at all, which shows that transformative works can sometimes evade Content ID entirely.

---

## **Gap Analysis: Law vs. Platform Policy vs. Actual Enforcement**

### **1. Legal Theory (Fair Use Doctrine)**

Under U.S. copyright law, fair use depends on a case-by-case analysis of the four factors. Pure reuploads of copyrighted media (Experiments 1 and 2) are generally not fair use. However, a commentary clip (Experiment 3) has a stronger argument for being transformative and legally permissible.

### **2. Platform Policy (What YouTube Says It Does)**

YouTube claims several points, such as: All uploads are scanned by Content ID, copyrighted material will be flagged if it matches known reference files, transformative uses may still be claimed automatically, and enforcement depends on rights holders, not YouTube. 

YouTube’s policy emphasizes that Content ID is an *automated matching system*, not a fair-use evaluator. This might explain why we get the checks so quickly - the content ID must have been scanned for my longer video. I have a feeling that YouTube disregards videos that are too short and consider them as edge cases. 

### **3. Actual Enforcement**

My three uploads show a mixed pattern:

* **7-second raw clip:** No detection, even though legally it is non-transformative.
* **30-second raw clip:** Detected instantly, claim applied. However, the creator said I am still allowed to post it. 
* **Caption/commentary clip:** No detection, even though it still contains copyrighted visuals.

### **Where the Gaps Are**

Here are some gaps that I discover from these experiments 
* The short raw clip slipped through despite being the least defensible legally, so the **Content ID did not enforce consistently**. YouTube might have let some shorter clips slip through, not to mention that my short clip only has music, but no singing yet. 
* **The system does not evaluate fair use.** It only matches fingerprints. My commentary clip might legally qualify as fair use, but the system simply didn’t match it.
* In my second experiment, the content was claimed but allowed. This does not reflect a legal judgment, but just a policy choice by the rights holder. This means that **rights holders control enforcement.** 
* Platforms like YouTube avoid legal interpretation and rely on automated detection, which can under-detect or mis-detect content.




# **Section 5: Appendix**

## **Screenshots**

All screenshots used in this report are stored in the **`/screenshots`** folder of this repository.
Each file name describes the experiment and the stage of the upload (for example: `exp1-upload.png`, `exp2-claim.png`, `ai2-output.png`).

## **Links to Uploaded Content**

Below are the links to the YouTube uploads used in Section 2 and Section 3.

* Original video (blink-182 I Miss You Official Video): *[https://www.youtube.com/watch?v=s1tAYmMjLdY&list=RDs1tAYmMjLdY&start_radio=1]*
* Short raw clip (7 seconds): *[https://www.youtube.com/watch?v=e0QFSOUaanU]*
* Longer raw clip (30 seconds): *[https://www.youtube.com/watch?v=ednjAtA10rw]*
* Clip with captions (commentary-style): *[https://www.youtube.com/watch?v=BXs9xo-rkxg]*
* AI-generated uploads: *[https://www.youtube.com/watch?v=WeuFXuo6vjg]*

If any videos were removed or set to private later, the links still show the original upload location.

## **Timestamps of Uploads and Detection**

For each experiment, I noted when the video was uploaded and when YouTube completed its automated copyright check:

* **Short raw clip (7 seconds):**

  * Upload time: [12/05/2025, 8:18 pm]
  * Detection result: *No issues found*
  * Detection timing: *Immediate—check completed in a few seconds*

* **Long raw clip (30 seconds):**

  * Upload time: [12/05/2025, 8:32 pm]
  * Detection result: *Copyright-protected content found; owner allows use*
  * Detection timing: *Immediate—Content ID identified the clip during the upload check*

* **Caption/Commentary-style clip:**

  * Upload time: [12/05/2025, 8:45 pm]
  * Detection result: *No copyright issues found*
  * Detection timing: *Immediate—no claims or warnings*

* **AI-generated images:**

  * Upload time: [12/05/2025, 9:12 pm]
  * No copyright claims for any AI-generated content
  * Detection timing: *Immediate—YouTube flagged nothing*

