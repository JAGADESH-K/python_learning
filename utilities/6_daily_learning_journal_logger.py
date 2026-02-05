from datetime import datetime

now = datetime.now().strftime("%d-%m-%Y - %I:%M:%p")

entry = input("Write you jurnel entry: ").strip()
rating_entry = int(input("⭐ Rate your learning (1-5): "))

rating = f"{'⭐' * rating_entry}"

#print(f"{rating}\n{'-' * 10}\n{entry}\n\n{'#' * 50}\n")

jurnal_entry = f"📅 {now}\n{'-'*10}\n{rating}\n{'-' * 10}\n{entry}\n\n{'#' * 50}\n " ""

with open('daily_jurnal.txt',"a",encoding="utf-8") as f:
    f.write(jurnal_entry)


