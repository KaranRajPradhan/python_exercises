prompt = "->"

def processor(processor_rate):
    if processor_rate < 3:
        return "Processor: i3"
    elif processor_rate <= 4:
        return "Processor: i5"
    elif processor_rate >= 5:
        return "Processor: i7"

def ram(ram_rate):
    if ram_rate < 3:
        return "RAM: 4 GB"
    elif ram_rate <= 4:
        return "RAM: 8 GB"
    elif ram_rate >= 5:    
        return "RAM: 16 GB"

def storage(storage_rate):
    if storage_rate < 3:
        return "Storage: 256 GB"
    elif storage_rate <= 4:
        return "Storage: 512 GB"
    elif storage_rate >= 5:
        return "Storage: 1 TB"

def ssd(boot_rate):
    if boot_rate < 3:
        return "SSD: 128 GB"
    elif boot_rate <= 4:
        return "SSD: 256 GB"
    elif boot_rate >= 5:
        return "SSD: 512 GB"

def budget(budget_rate):
    if budget_rate < 3:
        return -1
    elif budget_rate > 3:
        return 1
    else:
        return 0

# while True:
if __name__ == "__main__":      #to import in another file and not run the whole code(make module)
    print("Rate your choice of processor between 1 to 5")
    processor_rate = int(input(prompt))
    print("Rate your choice of RAM between 1 to 5")
    ram_rate = int(input(prompt))
    print("Rate your choice of storage between 1 to 5")
    storage_rate = int(input(prompt))
    print("Rate your speed of booting between 1 to 5")
    boot_rate = int(input(prompt))
    print("Rate your budget between 1 to 5")
    budget_rate = int(input(prompt))
    
    processor_rate += budget(budget_rate)
    ram_rate += budget(budget_rate)
    storage_rate += budget(budget_rate)
    boot_rate += budget(budget_rate)
    
    print(processor(processor_rate))
    print(ram(ram_rate))
    if boot_rate <= storage_rate:
        print(storage(storage_rate))
    else:
        print(ssd(storage_rate))