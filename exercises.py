import random

push_exercise = [
    {
        "name": "barbell bench press",
        "equipment": ["barbell", "bench", "weight plates"]
    },
    {
        "name": "dumbbell bench press",
        "equipment": ["dumbbells", "bench"]
    },
    {
        "name": "incline barbell bench press",
        "equipment": ["barbell", "bench", "weight plates"]
    },
    {
        "name": "overhead barbell press",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "overhead dumbell press",
        "equipment": ["dumbbells"]
    },
    {
        "name": "pushup",
        "equipment": ["none"]
    },
    {
        "name": "tricep pushdown",
        "equipment": ["cable machine"]
    },
    {
        "name": "barbell push press",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "dumbbell push press",
        "equipment": ["dumbbells"]
    },
    {
        "name": "barbell floor press",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "dumbbell floor press",
        "equipment": ["dumbbells"]
    }
]

pull_exercise = [
    {
        "name": "seated row",
        "equipment": ["cable machine"]
    },
    {
        "name": "lat pulldown",
        "equipment": ["cable machine"]
    },
    {
        "name": "bentover barbell row",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "bentover dumbbell row",
        "equipment": ["dumbbells"]
    },
    {
        "name": "pull-up",
        "equipment": ["none"]
    },
    {
        "name": "chin-up",
        "equipment": ["none"]
    },
    {
        "name": "bicep curl",
        "equipment": ["dumbbells"]
    },
    {
        "name": "face pull",
        "equipment": ["cable machine"]
    },
    {
        "name": "barbell upright row",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "dumbbell upright row",
        "equipment": ["dumbbells"]
    }
]

squat_exercise = [
    {
        "name": "barbell back squat",
        "equipment": ["barbell", "squat rack", "weight plates"]
    },
    {
        "name": "barbell front squat",
        "equipment": ["barbell", "squat rack", "weight plates"]
    },
    {
        "name": "goblet squat",
        "equipment": ["dumbbells"]
    },
    {
        "name": "jumping squat",
        "equipment": ["dumbbells"]
    },
    {
        "name": "barbell sumo squat",
        "equipment": ["barbell", "squat rack", "weight plates"]
    },
    {
        "name": "dumbbell sumo squat",
        "equipment": ["dumbbells"]
    },
    {
        "name": "barbell overhead squat",
        "equipment": ["barbell", "squat rack", "weight plates"]
    },
    {
        "name": "single leg squat",
        "equipment": ["none"]
    },
    {
        "name": "barbell box squat",
        "equipment": ["barbell", "squat rack", "weight plates", "bench"]
    },
]

lunge_exercise = [
    {
        "name": "barbell lunge",
        "equipment": ["barbell", "squat rack", "weight plates"]
    },
    {
        "name": "dumbbell forward lunge",
        "equipment": ["dumbbells"]
    },
    {
        "name": "dumbbell backward lunge",
        "equipment": ["dumbbells"]
    },
    {
        "name": "rear foot elevated split squat",
        "equipment": ["dumbbells", "bench"]
    },
     {
        "name": "front foot elevated split squat",
        "equipment": ["dumbbells", "weight plates"]
    },
     {
        "name": "side lunge",
        "equipment": ["dumbbells"]
    },
    {
        "name": "walking lunge",
        "equipment": ["none"]
    }
]

carry_exercise = [
    {
        "name": "farmers carry",
        "equipment": ["dumbbells"]
    },
    {
        "name": "front rack carry",
        "equipment": ["dumbbells"]
    },
    {
        "name": "suitcase carry",
        "equipment": ["dumbbells"]
    },
    {
        "name": "goblet carry",
        "equipment": ["dumbbells"]
    },
    {
        "name": "zercher carry",
        "equipment": ["barbell", "weight plates"]
    }
]

hinge_exercise = [
    {
        "name": "conventional deadlift",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "Romanian deadlift",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "barbell sumo deadlift",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "dumbbell sumo deadlift",
        "equipment": ["dumbbells"]
    },
    {
        "name": "single leg Romanian deadlift",
        "equipment": ["dumbbells"]
    },
    {
        "name": "good morning",
        "equipment": ["barbell", "weight plates", "squat rack"]
    },
    {
        "name": "barbell hip thrust",
        "equipment": ["barbell", "weight plates", "bench"]
    },
    {
        "name": "dumbbell hip thrust",
        "equipment": ["dumbbells", "bench"]
    }
]


def workout_gen():
    push = random.choice(push_exercise)
    pull = random.choice(pull_exercise)
    squat = random.choice(squat_exercise)
    lunge = random.choice(lunge_exercise)
    carry = random.choice(carry_exercise)
    hinge = random.choice(hinge_exercise)
	
    workout = {
        "Push exercise": {
            "name": push["name"],
            "equipment": push["equipment"]
        },
        "Pull exercise": {
            "name": pull["name"],
            "equipment": pull["equipment"]
        },
        "Squat exercise": {
            "name": squat["name"],
            "equipment": squat["equipment"]
        },
        "Lunge exercise": {
            "name": lunge["name"],
            "equipment": lunge["equipment"]
        },
        "Carry exercise": {
            "name": carry["name"],
            "equipment": carry["equipment"]
        },
        "Hinge exercise": {
            "name": hinge["name"],
            "equipment": hinge["equipment"]
        }
    }

    return workout

if __name__ == "__main__":
    workout = workout_gen()
    print(workout)


