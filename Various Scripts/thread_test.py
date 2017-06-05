def startScreenshots(self, output, quality, interval):
    print 'Starting taking screenshots...'
    print 'Output folder: ' + str(output)
    print 'Quality: ' + str(quality)
    print 'Interval: ' + str(interval)

    # Update attributes
    self.outputDir = output
    self.quality = quality
    self.interval = interval
    self.currentShot = 0

    # Start a thread to take screenshots
    self.done = False
    self.thread = threading.Thread(target=self._takeScreenshot)
    self.thread.start()

def stopScreenshots(self):
    print 'Stopped taking screenshots.'
    self.done = True
    self.thread.join()


def _takeScreenshot(self):
    # Run until we're done
    while not self.done:
        # Build scrot command
        fileNumber = str(self.currentShot)
        fileNumber = fileNumber.zfill(self.numDigits - len(fileNumber))
        fileName = 'scr-' + fileNumber + '.jpg'

        command = 'scrot -q ' + str(self.quality) + ' ' + self.outputDir + os.sep + fileName

        print 'Taking screenshot: ' + command + '...'

        os.system(command)

        # Schedule next screenshot
        print 'Scheduling next screenshot...'
        self.currentShot = self.currentShot + 1
        time.sleep(self.interval)
